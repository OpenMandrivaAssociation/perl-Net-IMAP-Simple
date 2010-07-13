%define upstream_name	 Net-IMAP-Simple
%define upstream_version 1.2000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Simple IMAP interface to Perl 5	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(Regexp::Common)

BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl extension for simple IMAP account handling, 
mostly compatible with Net::POP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

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
