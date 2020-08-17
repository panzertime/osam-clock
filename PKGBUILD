# Maintainer: ptime <panzer.time@gmail.com>
pkgname=osam-clock
pkgver=1.0
pkgrel=1
epoch=
pkgdesc="Clock with Old-Style Anno Mundi date"
arch=('any')
url="https://github.com/panzertime/osam-clock"
license=('MPL2')
makedepends=('python-setuptools')
source=("https://github.com/panzertime/osam-clock/raw/master/osam-clock.py")
md5sums=("b4a5044fba78b850871e93d67d9353d7")

package() {
	sudo cp "${srcdir}/osam-clock.py" "/usr/bin/osam-clock"
	sudo chmod a+x /usr/bin/osam-clock 
}
