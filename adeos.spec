Summary:	Adeos - automated filesystem security scanner
Summary(pl):	Adeos - Zautomatyzowany skaner bezpiecze�stwa systemu plik�w
Name:		adeos
Version:	1.0
Release:	1
Group:		Applications/System
License:	GPL v2
Source0:	http://linux.wku.edu/~lamonml/software/adeos/%{name}-%{version}.tar.bz2
URL:		http://linux.wku.edu/~lamonml/software/adeos/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adeos (named after the obscure Roman goddess of modesty) is an
automated filesystem security scanner. It recursively walks all
mounted filesystems on the local system and attempts to identify
common security concerns such as SUID and world-writeable files.

%description -l pl
Adeos (nazwany na cze�� nieznanego rzymskiego boga skromno�ci) jest
zautomatyzowanym skanerem bezpiecze�stwa systemu plik�w. Program
rekursywnie przemieszcza si� po lokalnym systemie plik�w i stara si�
zidentyfikowa� powszechne b��dy w zabezpieczeniach, takie jak SUIDy
czy pliki zapisywalne dla wszystkich.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
