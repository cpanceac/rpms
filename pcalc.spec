Name:           pcalc
Version:        5
Release:        1%{?dist}
Summary:        Command line util for doing hex/dec/oct/bin math quickly

License:        GPLv2
URL:            https://vapier.github.io/pcalc/
Source0:        https://github.com/vapier/pcalc/archive/refs/tags/v5.tar.gz

%description
Tool that converts between hexadecimal / decimal / octal / binary.
Features
    Full math parser, parentheses, add, sub, mult, div, exponential
    Automatic conversion between HEX DEC OCT BIN numbers
    Mixing different bases in one expression
    Definable variables
    Math constants (E PI ...)
    Built in math functions (sin/cos/sqrt ...)



%prep
%autosetup


%build
%make_build


%install
%make_install


%files
%{_bindir}/pcalc
/usr/lib/debug/usr/bin/pcalc-5-1.fc38.x86_64.debug


%license COPYING
%doc AUTHORS EXAMPLE TODO README.md



%changelog
* Fri May 12 2023 Cornel Panceac <cpanceac@gmail.com>
- 
