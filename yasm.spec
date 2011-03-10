Name: yasm
Version: 1.1.0
Summary: Modular Assembler
License: BSD and (GPLv2+ or Artistic or LGPLv2+) and LGPLv2
URL: http://www.tortall.net/projects/yasm/
Source: http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz

BuildRequires: developer/parser/bison

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License (some portions are under other licenses, see COPYING for details). It is designed from the ground up to allow for multiple assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object formats and even multiple instruction sets. Another primary module of the overall design is an optimizer module.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --disable-debug --disable-dependency-tracking
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean

%files
%defattr (-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*

