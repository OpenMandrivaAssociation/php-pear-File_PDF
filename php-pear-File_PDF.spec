%define		_class		File
%define		_subclass	PDF
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.3
Release:	16
Summary:	PDF generation using only PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_PDF/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package provides PDF generation using only PHP, without requiring
any external libraries.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
%{_datadir}/pear/test/File_PDF/tests/*


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-2mdv2012.0
+ Revision: 741758
- fix major breakage by careless packager

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-1
+ Revision: 735167
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-6
+ Revision: 667498
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-5mdv2011.0
+ Revision: 607100
- rebuild

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-4mdv2010.1
+ Revision: 478672
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.2-3mdv2010.0
+ Revision: 426629
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdv2009.1
+ Revision: 321813
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-1mdv2009.0
+ Revision: 272585
- 0.3.2

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-3mdv2009.0
+ Revision: 224734
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdv2008.1
+ Revision: 178509
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdv2008.0
+ Revision: 15670
- 0.2.0


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-8mdv2007.0
+ Revision: 83321
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-7mdv2007.1
+ Revision: 81586
- Import php-pear-File_PDF

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-1mdk
- initial Mandriva package (PLD import)

