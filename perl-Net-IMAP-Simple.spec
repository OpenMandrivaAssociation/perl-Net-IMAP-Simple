%define upstream_name	 Net-IMAP-Simple
%define upstream_version 1.2205

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simple IMAP interface to Perl 5	

License:	GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

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



