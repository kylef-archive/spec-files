Name: faac
Version: 1.28
License: GPL
URL: http://www.audiocoding.com/faac.html
Source: http://downloads.sourceforge.net/project/faac/faac-src/faac-%{version}/faac-%{version}.tar.gz

%prep
%setup -q

%build
CC=gcc
CXX=g++
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*
