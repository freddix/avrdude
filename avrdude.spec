Summary:	Software for programming Atmel AVR Microcontrollers
Name:		avrdude
Version:	5.11.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avrdude/%{name}-%{version}.tar.gz
# Source0-md5:	3a43e288cb32916703b6945e3f260df9
URL:		http://savannah.nongnu.org/projects/avrdude/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libusbx-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*

