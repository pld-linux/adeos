# TODO: webapps or so
Summary:	Adeos - automated filesystem security scanner
Summary(pl.UTF-8):   Adeos - Zautomatyzowany skaner bezpieczeństwa systemu plików
Name:		adeos
Version:	1.0
Release:	3
Group:		Applications/System
License:	GPL v2
Source0:	http://linux.wku.edu/~lamonml/software/adeos/%{name}-%{version}.tar.bz2
# Source0-md5:	059b47e4cd45a40c060bd41dd33739a1
URL:		http://linux.wku.edu/~lamonml/software/adeos/
BuildRequires:	fhs-compliance
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wwwdir		/srv/httpd/html/%{name}

%description
Adeos (named after the obscure Roman goddess of modesty) is an
automated filesystem security scanner. It recursively walks all
mounted filesystems on the local system and attempts to identify
common security concerns such as SUID and world-writeable files.

%description -l pl.UTF-8
Adeos (nazwany na cześć nieznanego rzymskiego boga skromności) jest
zautomatyzowanym skanerem bezpieczeństwa systemu plików. Program
rekursywnie przemieszcza się po lokalnym systemie plików i stara się
zidentyfikować powszechne błędy w zabezpieczeniach, takie jak SUIDy
czy pliki zapisywalne dla wszystkich.

%package www
Summary:	Adeos - automated filesystem security scanner
Summary(pl.UTF-8):   Adeos - Zautomatyzowany skaner bezpieczeństwa systemu plików
Group:		Applications/System
Requires:	adeos
Requires:	crondaemon
Requires:	webserver

%description www
Scripts and cron jobs to publish data on WWW.

%description www -l pl.UTF-8
Skrypty crona do publikacji na stronie WWW.

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

%files www
%defattr(644,root,root,755)
%dir %{_wwwdir}
%ghost %{_wwwdir}/results.html
%attr(755,root,root) %config(noreplace) /etc/cron.weekly/%{name}.sh
