%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	SmallProf
Summary:	Devel::SmallProf perl module
Summary(pl):	Modu� perla Devel::SmallProf
Name:		perl-Devel-SmallProf
Version:	0.9
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Time-HiRes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::SmallProf - per-line Perl profiler.

%description -l pl
Modu� perla Devel::SmallProf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/SmallProf.pm
%{_mandir}/man3/*
