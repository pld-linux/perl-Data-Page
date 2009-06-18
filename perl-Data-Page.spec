#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Page
Summary:	Data::Page - help when paging through sets of results
Summary(pl.UTF-8):	Data::Page - pomoc przy stronicowaniu zbiorów wyników
Name:		perl-Data-Page
Version:	2.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	301eeb65db5f6aeafa354978404f08d8
%if %{with tests}
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Test-Exception
%endif
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Class-Accessor-Chained
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When searching through large amounts of data, it is often the case
that a result set is returned that is larger than we want to display
on one page.  This results in wanting to page through various pages of
data. The maths behind this is unfortunately fiddly, hence this
module.

The main concept is that you pass in the number of total entries, the
number of entries per page, and the current page number. You can then
call methods to find out how many pages of information there are, and
what number the first and last entries on the current page really are.

%description -l pl.UTF-8
Przy przeszukiwaniu dużych ilości danych zwykle zwracany zbiór wyników
jest większy niż chcielibyśmy wyświetlić na jednej stronie. Powoduje
to chęć podzielenia danych na strony. Obliczenia przy tym są niestety
nietrywialne i stąd ten moduł.

Główną ideą jest to, że przekazuje się liczbę wszystkich elementów,
liczbę elementów na stronie i aktualny numer strony. Można wtedy
wywoływać metody, aby określić liczbę stron z informacjami oraz numer
pierwszego i ostatniego elementu na aktualnej stronie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Data/Page.pm
%{_mandir}/man3/*
