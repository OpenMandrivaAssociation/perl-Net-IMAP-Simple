%define module	Net-IMAP-Simple
%define name	perl-%{module}
%define version 1.17
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple IMAP interface to Perl 5	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Perl extension for simple IMAP account handling, 
mostly compatible with Net::POP.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%{makeinstall_std}

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Net

