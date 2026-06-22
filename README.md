# Contact Card

A single-file, dependency-free digital contact card (a.k.a. "link-in-bio" / digital business card)
designed for academics. Drop it on GitHub Pages and share the URL — or its QR code — on a poster,
slide, or business card.

![preview](headshot.jpg)

## Features

- **One file to edit.** All your details live in a single `CARD` object at the top of
  [`index.html`](index.html). Everything else renders from it.
- **No build step, no framework, no tracking.** Plain HTML/CSS/JS. Open it in a browser and it works.
- **Save-contact button.** Visitors download a standards-compliant `.vcf` (vCard 3.0) — including
  your photo — straight to their phone's address book. Works offline once the page is open.
- **Icon set built in.** Tag each link and it picks the matching SVG icon automatically.
- **Responsive & accessible.** Mobile-first layout, keyboard focus styles, and
  `prefers-reduced-motion` support.
- **QR generator included.** [`make_qr.py`](make_qr.py) turns your card's URL into a high
  error-correction PNG suitable for print.

## Repository contents

| File              | Purpose                                                              |
| ----------------- | ------------------------------------------------------------------- |
| `index.html`      | The contact card. Edit the `CARD` block, deploy the file.           |
| `make_qr.py`      | Generates `qr.png` from a URL (for posters/slides).                 |
| `requirements.txt`| Python dependency for `make_qr.py`.                                  |
| `headshot.jpg`    | Profile photo shown on the card and embedded in the vCard.          |
| `qr.png`          | Generated QR code (output of `make_qr.py`).                         |

## Quick start

### 1. Edit your details

Open `index.html` and edit only the `CARD` block near the top:

```js
const CARD = {
  photo:       "headshot.jpg",   // file in this folder; set "" to hide
  name:        "Your Name",
  title:       "PhD Candidate · Computer Science",
  affiliation: "Your Lab, Your University",
  links: [
    { tag: "EMAIL",    label: "you@example.edu", url: "mailto:you@example.edu" },
    { tag: "WEBSITE",  label: "yourname.github.io", url: "https://yourname.github.io" },
    { tag: "GITHUB",   label: "github.com/you", url: "https://github.com/you" },
  ],
  vcard: { email: "you@example.edu", phone: "+1234567890" }
};
```

Delete any line you don't want — it simply won't render.

**Valid link tags** (each picks its own icon):

```
EMAIL  PHONE  WEBSITE  PAPER  CV  SCHOLAR  ORCID
GITHUB  LINKEDIN  TWITTER  BLUESKY  RESEARCHGATE
```

Unknown tags fall back to the `WEBSITE` icon.

### 2. Preview locally

Open the file directly in a browser:

```sh
xdg-open index.html      # Linux
open index.html          # macOS
```

> The **Save contact** button fetches the photo to embed it in the vCard. Some browsers block
> `fetch` of local files via `file://`. To test that feature, serve the folder:
>
> ```sh
> python3 -m http.server 8000
> # then visit http://localhost:8000
> ```

### 3. Deploy (GitHub Pages)

1. Push this repo to GitHub.
2. **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Your card goes live at `https://<user>.github.io/<repo>/`.

## Generating the QR code

The QR generator needs Python 3 and the `qrcode` package.

```sh
python3 -m venv .qrenv          # optional virtual environment
source .qrenv/bin/activate
pip install -r requirements.txt

python make_qr.py https://yourname.github.io/contact/
# -> writes qr.png
```

`make_qr.py` uses high error-correction (`ERROR_CORRECT_H`), so the code stays scannable even if a
logo is overlaid or part of it is obscured — ideal for posters and slides.

## License

No license file is included. Add one (e.g. MIT) if you intend others to reuse this.
