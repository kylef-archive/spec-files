Name: c-ares
Version: 1.7.4
Summary: A library that performs asynchronous DNS operations
License: MIT
URL: http://c-ares.haxx.se/
Source: http://c-ares.haxx.se/c-ares-%{version}.tar.gz

%description
c-ares is a C library that performs DNS requests and name resolves 
asynchronously. c-ares is a fork of the library named 'ares', written 
by Greg Hudson at MIT.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --enable-shared --disable-static --disable-dependency-tracking
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcares.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README README.cares CHANGES NEWS
%{_libdir}/*.so.*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

