%define major 0
%define commit da46a25440ac4615daf7d7816f51b18cd65909df

Name:           wrapland
Version:        0.527.80
Release:        1
Summary:        C++ wrapper for the libwayland client and server API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://gitlab.com/kwinft/%{name}
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
Patch1:         EPROTO.patch

BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(KF6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  fdupes
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-scanner)
Provides:       libWraplandClient = %{version}

%description
Wrapland is a Qt/C++ library that wraps and mediates the libwayland
client and server API for its consumers. Wrapland is an independent
part of the KWinFT project with the KWinFT window manager being
first and most prominent user.

%package devel
Summary:        Wrapland: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       cmake(Microsoft.GSL)

%description devel
Client and Server library wrapper for the Wayland libraries.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license COPYING.LIB
%{_datadir}/qlogging-categories6/org_kde_wrapland.categories
%{_libdir}/libWraplandClient.so.%{major}*
%{_libdir}/libWraplandServer.so.%{major}*

%files devel
%{_includedir}/Wrapland/
%{_includedir}/wrapland_version.h
%{_libdir}/cmake/Wrapland/
%{_libdir}/libWraplandClient.so
%{_libdir}/libWraplandServer.so
