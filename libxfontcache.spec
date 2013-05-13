%define libxfontcache %mklibname xfontcache 1
Name: libxfontcache
Summary:  The Xfontcache Library
Version: 1.0.5
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfontcache-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The Xfontcache Library

#-----------------------------------------------------------

%package -n %{libxfontcache}
Summary:  The Xfontcache Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxfontcache}
The Xfontcache Library

#-----------------------------------------------------------

%package -n %{libxfontcache}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxfontcache} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxfontcache-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxfontcache}-devel
Development files for %{name}

%files -n %{libxfontcache}-devel
%defattr(-,root,root)
%{_libdir}/libXfontcache.so
%{_libdir}/pkgconfig/xfontcache.pc
%{_mandir}/man3/FontCache*
%{_mandir}/man3/Xfontcache*

#-----------------------------------------------------------

%package -n %{libxfontcache}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxfontcache}-devel = %{version}
Provides: libxfontcache-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxfontcache}-static-devel
Static development files for %{name}

%files -n %{libxfontcache}-static-devel
%defattr(-,root,root)
%{_libdir}/libXfontcache.a

#-----------------------------------------------------------

%prep
%setup -q -n libXfontcache-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxfontcache}
%defattr(-,root,root)
%{_libdir}/libXfontcache.so.1
%{_libdir}/libXfontcache.so.1.0.0


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-3mdv2011.0
+ Revision: 661558
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2011.0
+ Revision: 602619
- rebuild

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 463587
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-4mdv2010.0
+ Revision: 425921
- rebuild
- Use %%configure2_5x instead of %%configure to avoid an unneeded (and harmful for the build) call to libtoolize

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2009.0
+ Revision: 223074
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 153306
- Update BuildRequires and rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Feb 15 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.0
+ Revision: 121456
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

