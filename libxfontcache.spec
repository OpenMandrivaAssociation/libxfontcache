%define major 1
%define libname %mklibname xfontcache %{major}
%define devname %mklibname xfontcache -d

Summary:	The Xfontcache Library
Name:		libxfontcache
Version:	1.0.5
Release:	16
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfontcache-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The Xfontcache Library

%package -n %{libname}
Summary:	The Xfontcache Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The Xfontcache Library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	libxfontcache-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libXfontcache-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfontcache.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfontcache.so
%{_libdir}/pkgconfig/xfontcache.pc
%{_mandir}/man3/FontCache*
%{_mandir}/man3/Xfontcache*

