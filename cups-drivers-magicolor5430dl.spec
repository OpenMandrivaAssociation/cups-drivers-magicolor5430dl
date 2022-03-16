%define rname magicolor5430dl

Summary:	Cups Driver for KONICA MINOLTA magicolor 5430 DL
Name:		cups-drivers-%{rname}
Version:	1.8.1
Release:	29
License:	GPL
Group:		System/Printing
URL:		http://printer.konicaminolta.net/
Source0:	magicolor5430DL-%{version}.tar.gz
Patch0:		magicolor5430DL-shared_system_libs.diff
Patch1:		magicolor5430DL-1.8.1-automake-1.13.patch
Patch2:		magicolor5430DL-1.8.1-cups-2.2.patch
Patch3:		magicolor5430DL-lcms2.patch
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	jbig-devel
BuildRequires:	pkgconfig(lcms2)
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
%patch1 -p1 -b .automake-1_13
%patch2 -p1 -b .cups-2_2
%patch3 -p1 -b .lcms2

# Fix copy of CUPS headers in kmlf.h
perl -p -i -e 's:\bcups_strlcpy:_cups_strlcpy:g' src/kmlf.h

# Remove asterisks from group names in PPD file
gzip -dc src/km_en.ppd.gz | perl -p -e 's/(Group:\s+)\*/$1/g' | gzip > src/km_en.tmp.ppd.gz && mv -f src/km_en.tmp.ppd.gz src/km_en.ppd.gz

# Determine the directory for the CUPS filters using the correct method
perl -p -i -e 's:(CUPS_SERVERBIN=)"\$libdir/cups":$1`cups-config --serverbin`:' configure*

%build
rm -f configure
libtoolize --force --copy; aclocal; automake --add-missing --copy --foreign; autoconf

%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog
%{_prefix}/lib/cups/filter/rastertokm5430dl
%{_datadir}/KONICA_MINOLTA/mc5430DL
%attr(0644,root,root) %{_datadir}/cups/model/KONICA_MINOLTA/km5430dl.ppd*
