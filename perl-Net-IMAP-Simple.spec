%define upstream_name	 Net-IMAP-Simple
%define upstream_version 1.2204

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Simple IMAP interface to Perl 5	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-IMAP-Simple-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(DateTime::Format::Mail)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::MIME)
BuildArch:	noarch

%description
Perl extension for simple IMAP account handling, 
mostly compatible with Net::POP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Net


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.202.300-1mdv2011.0
+ Revision: 684778
- update to new version 1.2023

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.202.200-1
+ Revision: 659980
- update to new version 1.2022

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.900-1mdv2011.0
+ Revision: 623082
- update to new version 1.2019

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.201.800-1mdv2011.0
+ Revision: 596625
- update to 1.2018

* Fri Sep 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.201.600-1mdv2011.0
+ Revision: 575593
- update to 1.2016

* Thu Sep 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.201.500-1mdv2011.0
+ Revision: 575398
- update to 1.2015

* Sun Aug 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.201.200-1mdv2011.0
+ Revision: 569941
- update to 1.2012

* Fri Jul 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.200.100-1mdv2011.0
+ Revision: 553968
- update to 1.2001

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 552458
- update to 1.2000

* Mon Apr 26 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.191.200-1mdv2010.1
+ Revision: 539087
- update to 1.1912

* Mon Mar 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.191.100-1mdv2010.1
+ Revision: 519953
- update to 1.1911

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.191.0-1mdv2010.1
+ Revision: 461333
- update to 1.1910

* Thu Aug 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.190.700-1mdv2010.0
+ Revision: 410682
- update to 1.1907

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.190.500-1mdv2010.0
+ Revision: 398942
- typo in buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- update to 1.1905

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2010.0
+ Revision: 396223
- update to new version 1.1900

* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.180.100-1mdv2010.0
+ Revision: 393569
- wrong name during spec cleanup
- update to 1.1801
- using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.17-4mdv2009.0
+ Revision: 258013
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.17-3mdv2009.0
+ Revision: 246118
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.17-1mdv2008.1
+ Revision: 136304
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2008.0
+ Revision: 77706
- new version


* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2007.0
- new version

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.14-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdk
- New release 1.14
- %%mkrel

* Fri Sep 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdk
- new release
- spec cleanup

* Mon Aug 01 2005 Pixel <pixel@mandriva.com> 0.103-1mdk
- new release

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.99-1mdk
- 0.99

* Thu Jul 08 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.95-1mdk
- 0.95

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.94-1mdk
- 0.94
- drop prefix tag

* Mon Dec 01 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.93-1mdk
- first Mandrake release, optional feature for nocatauth




