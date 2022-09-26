# Maintainer: AnClark Liu <anclarkliu@outlook.com>

pkgname=rime-pinyin-genshin-impact
pkgver=$(date +%Y%m%d)
pkgrel=1
pkgdesc='Fcitx 5 Pinyin Dictionary of Genshin Impact (from Bilibili Game Wiki)'
arch=('x86_64')
url='https://github.com/outloudvi/mw2fcitx'
license=('custom')
options=('!emptydirs')
source=('config.py')
sha256sums=('SKIP')
makedepends=('python-virtualenv')

prepare() {
  virtualenv3 "$srcdir"/venv
  cd "$srcdir"/venv
  "$srcdir"/venv/bin/pip install mw2fcitx
}

build() {
  cd "$srcdir"

  "$srcdir"/venv/bin/mw2fcitx
}

package() {
  RIME_DATA_DIR="$pkgdir"/usr/share/rime-data/
  mkdir -p $RIME_DATA_DIR
  cp "$srcdir"/GenshinImpact.dict.yml $RIME_DATA_DIR/GenshinImpact.dict.yaml
}

# vim: ts=2 sw=2 et:
