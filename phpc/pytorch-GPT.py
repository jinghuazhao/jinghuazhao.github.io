# Loading Data

# Importing torch specific modules
import torch
import torch.nn as nn
from torch.nn import functional as F

# Downloading the Shakespeare text file
!wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

# Reading the text file
text = open('input.txt', 'r').read()
vocab = sorted(list(set(text)))
encode = lambda s: [vocab.index(c) for c in s]
decode = lambda l: [vocab[c] for c in l]

# Testing encoding and decoding
ids = encode("I like to eat")
txt = decode(ids)
print(f"ids: {ids}")
print(f"txt: {txt}")
print("".join(txt))

# Splitting Data and Batching

# Splitting the data with a 90/10 train/validation split
x = int(0.9 * len(text))
text = torch.tensor(encode(text), dtype=torch.long)
train, val = text[:x], text[x:]

batch_size = 32
block_size = 8
device = 'cuda' if torch.cuda.is_available() else 'cpu'

def get_batch(split):
    data = train if split == 'train' else val
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

xb, yb = get_batch('train')

# Bigram Language Model

class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, embed_size)
        self.positional_embedding = nn.Embedding(block_size, embed_size)
        self.linear = nn.Linear(embed_size, vocab_size)
        self.block = nn.Sequential(*[Block(embed_size, num_head) for _ in range(num_layers)])
        self.layer_norm = nn.LayerNorm(embed_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        logits = self.token_embedding_table(idx)
        ps = self.positional_embedding(torch.arange(T, device=device))
        x = logits + ps
        logits = self.block(x)
        logits = self.linear(self.layer_norm(logits))

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            crop_idx = idx[:, -block_size:].to(device)
            logits, _ = self(crop_idx)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1).to(device)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx

# Attention Mechanism

class Head(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.key = nn.Linear(embed_size, head_size, bias=False)
        self.query = nn.Linear(embed_size, head_size, bias=False)
        self.value = nn.Linear(embed_size, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        v = self.value(x)
        wei = q @ k.transpose(2, 1) / self.head_size ** 0.5
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        wei = F.softmax(wei, dim=2)
        wei = self.dropout(wei)
        out = wei @ v
        return out

# Multi-Head Attention

class MultiHeadAttention(nn.Module):
    def __init__(self, head_size, num_head):
        super().__init__()
        self.sa_head = nn.ModuleList([Head(head_size) for _ in range(num_head)])
        self.dropout = nn.Dropout(dropout)
        self.proj = nn.Linear(embed_size, embed_size)

    def forward(self, x):
        x = torch.cat([head(x) for head in self.sa_head], dim=-1)
        x = self.dropout(self.proj(x))
        return x

# Feed-Forward Network

class FeedForward(nn.Module):
    def __init__(self, embed_size):
        super().__init__()
        self.ff = nn.Sequential(
            nn.Linear(embed_size, 4 * embed_size),
            nn.ReLU(),
            nn.Linear(4 * embed_size, embed_size),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.ff(x)

# Transformer Block

class Block(nn.Module):
    def __init__(self, embed_size, num_head):
        super().__init__()
        head_size = embed_size // num_head
        self.multihead = MultiHeadAttention(head_size, num_head)
        self.ff = FeedForward(embed_size)
        self.ll1 = nn.LayerNorm(embed_size)
        self.ll2 = nn.LayerNorm(embed_size)

    def forward(self, x):
        x = x + self.multihead(self.ll1(x))
        x = x + self.ff(self.ll2(x))
        return x

# Model Training

m = BigramLanguageModel(len(vocab)).to(device)
optimizer = torch.optim.AdamW(m.parameters(), lr=1e-3)

batch_size = 32
for epoch in range(5000):
    if epoch % 1000 == 0:
        m.eval()
        val_loss = 0.0
        for k in range(200):
            x, y = get_batch(True)
            _, val_loss_batch = m(x, y)
            val_loss += val_loss_batch.item()
        avg_val_loss = val_loss / (k + 1)
        print(f"Validation loss: {avg_val_loss}")
        m.train()

    xb, yb = get_batch('train')
    optimizer.zero_grad()
    _, loss = m(xb, yb)
    loss.backward()
    optimizer.step()

# Testing Generation

# Generate a text sequence
context = torch.zeros((1, 1), dtype=torch.long, device=device)
print("".join(decode(m.generate(context, max_new_tokens=100)[0].tolist())))
