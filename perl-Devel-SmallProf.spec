#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	SmallProf
Summary:	Devel::SmallProf - per-line Perl profiler
Summary(pl.UTF-8):   Devel::SmallProf - system wspomagania programowania w Perlu
Name:		perl-Devel-SmallProf
Version:	1.15
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c69cc531a507a29af945804cb4e6145c
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::SmallProf profiler is focused on the time taken for a
program run on a line-by-line basis.  It is intended to be as "small"
in terms of impact on the speed and memory usage of the profiled
program as possible and also in terms of being simple to use.

%description -l pl.UTF-8
System wspomagania programowania w Perlu Devel::SmallProf jest
zogniskowany na ilość czasu, potrzebnego na wykonanie poszczególnych
wierszy programu. Powinien on być na tyle mały, aby, o ile to możliwe,
nie wpływał na szybkość i zużycie pamięci analizowanego programu.
Powinien być też prosty w użyciu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
