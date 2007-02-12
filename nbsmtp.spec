Summary:	Simple mailer
Summary(pl.UTF-8):   Prosty program do wysyłania e-maili
Name:		nbsmtp
Version:	1.00
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://www.it.uc3m.es/~ferdy/nbsmtp/%{name}-%{version}.tar.gz
# Source0-md5:	f34952f0b5e5101035357ea1c7ed6bd2
Patch0:		%{name}-Makefile.patch
URL:		http://nbsmtp.ferdyx.org/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nbSMTP is a simple SMTP client suitable to run in chroot jails, in
embedded systems, laptops, workstations. It's written in C and it
compiles and runs under lot of Unix flavors such as Linux, MacOSX, or
FreeBSD.

%description -l pl.UTF-8
nbSMTP jest prostym klientem SMTP odpowiednim do uruchamiania w
chronionym środowisku, w systemach osadzonych, na laptopach, stacjach
roboczych. Jest napisany w C, kompiluje się i uruchamia na praktycznie
każdej uniksowej platformie takiej jak Linux, MacOSX czy FreeBSD.

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--enable-ssl \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS DOCS README.OSX
%attr(755,root,root) %{_bindir}/nbsmtp
%{_mandir}/man?/*
