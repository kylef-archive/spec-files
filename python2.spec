%define pybasever 2.7

Name: python2
Version: 2.7.1
Summary: An interpreted, interactive, object-oriented programming language
License: Python
URL: http://www.python.org/
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2

BuildRequires: library/readline
BuildRequires: library/ncurses
BuildRequires: library/security/openssl
BuildRequires: library/zlib
BuildRequires: library/expat

Requires: library/expat
Requires: library/security/openssl
Requires: library/zlib

%description
Python is an interpreted, interactive, object-oriented programming language often compared to Tcl, Perl, Scheme or Java. Python includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems (X11, Motif, Tk, Mac and MFC).

%prep
%setup -q -n Python-%{version}

%build
./configure --prefix=%{_prefix} \
            --enable-shared \
            --with-threads \
            --enable-ipv6 \
            --with-system-expat
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" altinstall maninstall

ln -sf python%{pybasever} $RPM_BUILD_ROOT%{_bindir}/python2
ln -sf python%{pybasever}-config $RPM_BUILD_ROOT%{_bindir}/python2-config

mv $RPM_BUILD_ROOT%{_bindir}/idle{,2}
mv $RPM_BUILD_ROOT%{_bindir}/pydoc{,2}
mv $RPM_BUILD_ROOT%{_bindir}/2to3{,-%{pybasever}}

# clean up shebangs
find "$RPM_BUILD_ROOT%{_libdir}/python%{pybasever}/" -name '*.py' | \
    xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/env python2|"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/*
