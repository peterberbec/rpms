# $Id$
# Authority: dries
# Upstream: Joe McMahon <mcmahon$ibiblio,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-DateTime

Summary: Support for converting dates to xsd:dateTime format
Name: perl-SOAP-DateTime
Version: 0.02
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-DateTime/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-DateTime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a little utility module that converts dates into the
format required by the SOAP 'xsd:dateTime' type.  It's just a
dumb little wrapper around Date::Manip, because that's the
lazy way to make sure that we are forgiving in what we accept.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SOAP/DateTime.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
