Summary:	Adeos - automated filesystem security scanner
Summary(pl):	Adeos - Zautomatyzowany skaner bezpieczeñstwa systemu plików
Name:		adeos
Version:	1.0
Release:	1
Group:		Applications/System
License:	GPL v2
Source0:	http://linux.wku.edu/~lamonml/software/adeos/%{name}-%{version}.tar.bz2
Requires:	crondaemon
Requires:	webserver
URL:		http://linux.wku.edu/~lamonml/software/adeos/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wwwdir		/home/httpd/html/%{name}

%description
Adeos (named after the obscure Roman goddess of modesty) is an
automated filesystem security scanner. It recursively walks all
mounted filesystems on the local system and attempts to identify
common security concerns such as SUID and world-writeable files.

%description -l pl
Adeos (nazwany na cze¶æ nieznanego rzymskiego boga skromno¶ci) jest
zautomatyzowanym skanerem bezpieczeñstwa systemu plików. Program
rekursywnie przemieszcza siê po lokalnym systemie plików i stara siê
zidentyfikowaæ powszechne b³êdy w zabezpieczeniach, takie jak SUIDy
czy pliki zapisywalne dla wszystkich.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/cron.weekly,%{_wwwdir}}

install %{name}	$RPM_BUILD_ROOT%{_bindir}

cat > $RPM_BUILD_ROOT/etc/cron.weekly/%{name}.sh <<EOF
cd %{_wwwdir}
%{_bindir}/%{name} -h
chmod a+r results.html
EOF

touch $RPM_BUILD_ROOT%{_wwwdir}/results.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%dir %{_wwwdir}
%ghost %{_wwwdir}/results.html
%attr(755,root,root) %config(noreplace) /etc/cron.weekly/%{name}.sh
