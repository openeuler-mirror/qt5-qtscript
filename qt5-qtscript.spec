# spec file for qt5-qtscript

%global qt_module qtscript

Name:    qt5-%{qt_module}
Version: 5.11.1
Release: 5
Summary: QtScript component for qt5
License: LGPLv2 with exceptions or GPLv3 with exceptions
URL:     http://www.qt.io

%global major_minor %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/new_archive/qt/5.11/5.11.1/submodules/qtscript-everywhere-src-5.11.1.tar.xz

BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel qt5-qtbase-private-devel


%package devel
Summary: Development files for %{name}
Provides: %{name}-private-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}

%package help
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description
This package provides support for qt5 application scripting with ECMAScript

%description devel
Development files for qt5-qtscript

%description help
Examples files for %{name}


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
%qmake_qt5
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" -e "/^QMAKE_PRL_LIBS/d" %{buildroot}%{_qt5_libdir}/*.prl
rm -fv %{buildroot}%{_qt5_libdir}/lib*.la

%files
%license LICENSE.LGPL*
%{_qt5_libdir}/libQt5Script.so.5*
%{_qt5_libdir}/libQt5ScriptTools.so.5*

%files devel
%{_qt5_headerdir}/Qt*/
%{_qt5_libdir}/libQt5Script.so
%{_qt5_libdir}/libQt5Script.prl
%{_qt5_libdir}/libQt5ScriptTools.so
%{_qt5_libdir}/libQt5ScriptTools.prl

%dir %{_qt5_libdir}/cmake/Qt5Script/
%{_qt5_libdir}/cmake/Qt5Script/Qt5ScriptConfig*.cmake

%dir %{_qt5_libdir}/cmake/Qt5ScriptTools/
%{_qt5_libdir}/cmake/Qt5ScriptTools/Qt5ScriptToolsConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5*.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri

%files help
%{_qt5_examplesdir}/


%changelog
* Fri Sep 18 2020 liuweibo <liuweibo10@huawei.com> - 5.11.1-5
- Fix Source0

* Fri Feb 14 2020 lingsheng <lingsheng@huawei.com> - 5.11.1-4
- Package init
