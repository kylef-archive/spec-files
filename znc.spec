%define _version 0.096

Name:           znc
Summary:        ZNC is an IRC bouncer
Version:        0.96
License:        GPLv2
Source:         http://znc.in/releases/archive/%{name}-%{_version}.tar.gz
URL:            http://znc.in/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: library/security/openssl
BuildRequires: c-ares

%description
ZNC is an IRC bouncer with many advanced features like detaching, multiple users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, Perl and C++ module support to name a few.

%prep
%setup -q -n %{name}-%{_version}

%build
./configure CC=gcc CXX=g++ --prefix=%{_prefix} --enable-extra
gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_bindir}/znc
%{_bindir}/znc-buildmod
%{_bindir}/znc-config
%{_prefix}/lib/znc/*.so
%{_prefix}/share/znc/*
%{_mandir}/man1/znc*
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/znc/

