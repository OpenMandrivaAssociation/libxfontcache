%define libxfontcache %mklibname xfontcache 1
Name: libxfontcache
Summary:  The Xfontcache Library
Version: 1.0.4
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfontcache-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
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
%{_libdir}/libXfontcache.la
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxfontcache}
%defattr(-,root,root)
%{_libdir}/libXfontcache.so.1
%{_libdir}/libXfontcache.so.1.0.0


