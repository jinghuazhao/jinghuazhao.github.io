
## Download images

```bash
python3 download_images.py
```

```
image_download/
├── download_images.py
├── images.csv
├── images_downloaded.csv
└── downloaded_images/
    ├── 01___Introduction_Section_image.jpg
    ├── 02___Introduction_Section_background.jpg
    ├── 03___Services_Service_1.jpg
    ├── ...
    ├── 14_blog_...jpg
    └── 15_blog_...jpg
```

## Replace images

```bash
mkdir -p assets/images
mv downloaded_images/* assets/images/
python3 update_image_references.py
```

```
# python3 update_image_references.py
zetianmiaomu/
├── index.html
├── blog.html
├── assets/
│   ├── site.css
│   ├── bootstrap.bundle.min.js
│   └── images/
└── blog/
    ├── -9c06deb1.html
    ├── 2024-4daa6343.html
    └── -7e64aeef.html
```

## Start afresh

```bash
cd ~/Downloads
cp ~/jinghuazhao.github.io/docs/zetianmiaomu/images.csv .
python3 ~/jinghuazhao.github.io/docs/zetianmiaomu/download_images.py
module load ceuadmin/python/3.14.10
python3 migrate_solo_site.py \
  ~/Downloads/solo-websites-20261118203431.zip \
  --images ~/Downloads/downloaded_images \
  --output ~/tests/zetianmiaomu
```

## Check results

```bash
python3 -m http.server 8000 &
firefox http://localhost:8000/ &
zip -r zetianmiaomu-local.zip \
    index.html blog.html blog assets images.csv \
    images_downloaded.csv README-local.txt
```
