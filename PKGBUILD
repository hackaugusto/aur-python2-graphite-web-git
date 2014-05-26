# Maintainer: Augusto F. Hack <hack.augusto@gmail.com>
pkgname=python2-graphite-web-git
pkgver=0.9.12
pkgrel=1
pkgdesc="A highly scalable real-time graphing system"
arch=('x86_64')
url="https://github.com/graphite-project/graphite-web"
license=('apache')
depends=('django-tagging'
         'python2'
         'python2-cairo'
         'python2-django'
         'python2-pytz'
         'python2-simplejson'
         'python2-sphinx'
         'python2-pysqlite'
         'python2-whisper-git'
         'python2-pyparsing')
optdepends=('python2-ldap: authentication backend'
            'gunicorn-python2'
            'apache'
            'nginx'
            'python2-memcached: improved performance')
makedepends=('git' 'python2')
backup=('etc/graphite/graphTemplates.conf'
        'etc/graphite/dashboard.conf'
        'etc/httpd/sites-available/graphite.conf'
        'etc/nginx/sites-available/graphite.conf'
        'etc/uwsgi/sites-available/graphite.ini'
        'etc/graphite/graphite_settings.py')
source=('graphite::git+https://github.com/graphite-project/graphite-web.git'
        'local_settings.py'
        'settings.py'
        'graphite_apache.conf'
        'graphite_nginx.conf'
        'graphite_uwsgi.ini'
        'graphite-manage.py')
md5sums=('SKIP'
         '75e25c82d44888e2b76ed60a96c3c4fa'
         '7833f8d6acb209bd7de7692aabeb0f5f'
         '92eca15d6c8ff4ee1e051a7188401bc4'
         '16b34823edbba107fc5267b59f2f8dfe'
         '7ce24cd82e299b93e4c0d6cc811afd1f'
         '2f6db163ae8cd9fdb57f6b5d634bac6c')
install=graphite.install

pkgver() {
  cd "$srcdir/repo"
  git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

package() {
  cd "$srcdir/graphite"

  python2 setup.py install --root="$pkgdir/" --install-lib=/usr/lib/python2.7/site-packages --install-data=/usr/share/graphite-web --install-scripts=/usr/bin --optimize=1

  install -D -m644 $srcdir/graphite/conf/dashboard.conf.example $pkgdir/etc/graphite/dashboard.conf
  install -D -m644 $srcdir/graphite/conf/graphTemplates.conf.example $pkgdir/etc/graphite/graphTemplates.conf
  rm $pkgdir/usr/lib/python2.7/site-packages/graphite/local_settings.py.example
  rm $pkgdir/usr/bin/run-graphite-devel-server.py
  rm $pkgdir/usr/bin/build-index.sh

  install -D -m744 $srcdir/graphite-manage.py $pkgdir/usr/bin/graphite-manage.py

  # we install the django settings in the /etc/graphite and add it to the sys.path
  install -D -m644 $srcdir/settings.py $pkgdir/usr/lib/python2.7/site-packages/graphite/settings.py
  install -D -m644 $srcdir/local_settings.py $pkgdir/etc/graphite/graphite_settings.py
  install -D -m644 $srcdir/graphite_apache.conf $pkgdir/etc/httpd/sites-available/graphite.conf
  install -D -m644 $srcdir/graphite_nginx.conf $pkgdir/etc/nginx/sites-available/graphite.conf
  install -D -m644 $srcdir/graphite_uwsgi.ini $pkgdir/etc/uwsgi/sites-available/graphite.ini

  install -D -m755 -o http -g http -d $pkgdir/var/log/graphite
  install -D -m755 -o http -g http -d $pkgdir/var/lib/graphite
}

# vim:set ts=2 sw=2 et:
