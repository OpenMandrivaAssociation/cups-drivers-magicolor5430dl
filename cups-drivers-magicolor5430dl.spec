%define rname magicolor5430dl

Summary:	Cups Driver for KONICA MINOLTA magicolor 5430 DL
Name:		cups-drivers-%{rname}
Version:	1.8.1
Release:	23
License:	GPL
Group:		System/Printing
URL:		http://printer.konicaminolta.net/
Source0:	magicolor5430DL-%{version}.tar.gz
Patch0:		magicolor2430DL-shared_system_libs.diff
Patch1:		magicolor-automake-1.13.patch
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	jbig-devel
BuildRequires:	lcms-devel
Requires:	cups
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm5430dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 5430 DL printer

%prep

%setup -q -n magicolor5430DL-%{version}
%patch0 -p0
%patch1 -p1 -b .am113~

# Fix copy of CUPS headers in kmlf.h
perl -p -i -e 's:\bcups_strlcpy:_cups_strlcpy:g' src/kmlf.h

# Remove asterisks from group names in PPD file
gzip -dc src/km_en.ppd.gz | perl -p -e 's/(Group:\s+)\*/$1/g' | gzip > src/km_en.tmp.ppd.gz && mv -f src/km_en.tmp.ppd.gz src/km_en.ppd.gz

# Determine the directory for the CUPS filters using the correct method
perl -p -i -e 's:(CUPS_SERVERBIN=)"\$libdir/cups":$1`cups-config --serverbin`:' configure*

%build
rm -f configure
libtoolize --force --copy; aclocal; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_prefix}/lib/cups/filter/rastertokm5430dl
%{_datadir}/KONICA_MINOLTA/mc5430DL
%attr(0644,root,root) %{_datadir}/cups/model/KONICA_MINOLTA/km5430dl.ppd*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-13mdv2011.0
+ Revision: 663443
- mass rebuild

* Sun Jan 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-12mdv2011.0
+ Revision: 627567
- don't force the usage of automake1.7

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-11mdv2011.0
+ Revision: 603875
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-10mdv2010.1
+ Revision: 518847
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-9mdv2010.0
+ Revision: 413291
- rebuild

* Sat Jan 31 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-8mdv2009.1
+ Revision: 335840
- rebuilt against new jbigkit major

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-7mdv2009.1
+ Revision: 318075
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.8.1-6mdv2009.0
+ Revision: 220546
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.8.1-5mdv2008.1
+ Revision: 149153
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-4mdv2008.0
+ Revision: 75332
- fix deps (pixel)

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 1.8.1-3mdv2008.0
+ Revision: 69002
- fix description

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2mdv2008.0
+ Revision: 64153
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-1mdv2008.0
+ Revision: 62516
- Import cups-drivers-magicolor5430dl



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-1mdv2008.0
- initial Mandriva package
