#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: a19cdc7
#
Name     : pypi-blosc2
Version  : 2.7.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/ef/bb/19a5d672f86dd26be0fc4f3a4c04264c088f3309b7b9d4e3e853a1f3cfda/blosc2-2.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/bb/19a5d672f86dd26be0fc4f3a4c04264c088f3309b7b9d4e3e853a1f3cfda/blosc2-2.7.1.tar.gz
Summary  : Python wrapper for the C-Blosc2 library
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT Zlib
Requires: pypi-blosc2-license = %{version}-%{release}
Requires: pypi-blosc2-python = %{version}-%{release}
Requires: pypi-blosc2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : c-blosc2-dev
BuildRequires : cmake
BuildRequires : ninja
BuildRequires : pypi(cython)
BuildRequires : pypi(ninja)
BuildRequires : pypi(numpy)
BuildRequires : pypi(scikit_build)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-cython
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=============
Python-Blosc2
=============
A Python wrapper for the extremely fast Blosc2 compression library
==================================================================

%package license
Summary: license components for the pypi-blosc2 package.
Group: Default

%description license
license components for the pypi-blosc2 package.


%package python
Summary: python components for the pypi-blosc2 package.
Group: Default
Requires: pypi-blosc2-python3 = %{version}-%{release}

%description python
python components for the pypi-blosc2 package.


%package python3
Summary: python3 components for the pypi-blosc2 package.
Group: Default
Requires: python3-core
Provides: pypi(blosc2)
Requires: pypi(msgpack)
Requires: pypi(ndindex)
Requires: pypi(numexpr)
Requires: pypi(numpy)
Requires: pypi(py_cpuinfo)

%description python3
python3 components for the pypi-blosc2 package.


%prep
%setup -q -n blosc2-2.7.1
cd %{_builddir}/blosc2-2.7.1

%build
## build_prepend content
export CMAKE_ARGS="-DUSE_SYSTEM_BLOSC2=ON"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729491896
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-blosc2
cp %{_builddir}/blosc2-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/97a5f8f1173c4a9cd3f595fc54417d510bd076f9 || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/f95d3411831b0a3233ecbba99b85d2f1688773cd || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSES/BITSHUFFLE.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/d1b152dfd8ac42778f5d4aacfb62b92bf2ab4145 || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSES/FASTLZ.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/7f9f00bd71460bbd6551c361fe5e95023ab69ebd || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSES/LZ4.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/63aa9e87fdd44f2c9627db9a6b6d29a95e6ef53d || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSES/ZLIB.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/1e0b08e7a2124c67c42261ac819e2340a2dd912c || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/LICENSES/ZSTD.txt %{buildroot}/usr/share/package-licenses/pypi-blosc2/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c || :
cp %{_builddir}/blosc2-%{version}/blosc2/c-blosc2/internal-complibs/zlib-ng-2.0.7/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-blosc2/1e0b08e7a2124c67c42261ac819e2340a2dd912c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-blosc2/1e0b08e7a2124c67c42261ac819e2340a2dd912c
/usr/share/package-licenses/pypi-blosc2/63aa9e87fdd44f2c9627db9a6b6d29a95e6ef53d
/usr/share/package-licenses/pypi-blosc2/7f9f00bd71460bbd6551c361fe5e95023ab69ebd
/usr/share/package-licenses/pypi-blosc2/97a5f8f1173c4a9cd3f595fc54417d510bd076f9
/usr/share/package-licenses/pypi-blosc2/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
/usr/share/package-licenses/pypi-blosc2/d1b152dfd8ac42778f5d4aacfb62b92bf2ab4145
/usr/share/package-licenses/pypi-blosc2/f95d3411831b0a3233ecbba99b85d2f1688773cd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
