%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	SmallProf
Summary:	Devel::SmallProf perl module
Summary(pl):	Modu³ perla Devel::SmallProf
Name:		perl-Devel-SmallProf
Version:	1.11
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0c690c96caf7b78273609caff883ffc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Time-HiRes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::SmallProf - per-line Perl profiler.

%description -l pl
Modu³ perla Devel::SmallProf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Devel/SmallProf.pm
%{_mandir}/man3/*
