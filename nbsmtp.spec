Summary:	Simple mailer
Summary(pl):	Prosty program do wysy³ania e-maili
Name:		nbsmtp
Version:	0.98
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://www.it.uc3m.es/~ferdy/nbsmtp/%{name}-%{version}.tar.gz
# Source0-md5:	fe055f4e01e6cfd9eb9c80681a42f7eb
Patch0:		%{name}-Makefile.patch
URL:		http://nbsmtp.ferdyx.org/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nbSMTP is a simple SMTP client suitable to run in chroot jails, in
embedded systems, laptops, workstations. It's written in C and it
compiles and runs under lot of Unix flavors such as Linux, MacOSX, or
FreeBSD.

%description -l pl
nbSMTP jest prostym klientem SMTP odpowiednim do uruchamiania w
chronionym ¶rodowisku, w systemach osadzonych, na laptopach, stacjach
roboczych. Jest napisany w C, kompiluje siê i uruchamia na praktycznie
ka¿dej uniksowej platformie takiej jak Linux, MacOSX czy FreeBSD.

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--enable-ssl

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
