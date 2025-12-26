Name:		psautohint
Summary:	A standalone version of AFDKO’s autohinter
Version:	2.0.0
Release:	2
License:	ASL 2.0
Group:		Text tools
Url:		https://github.com/adobe-type-tools/psautohint
Source0:	https://github.com/adobe-type-tools/psautohint/releases/download/v%{version}/psautohint-%{version}.zip
#Patch0:		psautohint-1.8.1-linking.patch
BuildRequires:	python3-devel
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)

%description
psautohint is a standalone version of the autohinter from the Adobe Font
Development Kit for OpenType (AFDKO).

%package -n python-psautohint
Summary:	Python library for standalone version of the AFDKO autohinter
Group:		Development/Python
Provides:	%{name} = %{version}-%{release}
%{?python_provide:%python_provide python-psautohint}

%description -n python-psautohint
psautohint is a standalone version of the autohinter from the Adobe Font
Development Kit for OpenType (AFDKO).

%prep
%autosetup -p1

# re-generate egg-info
rm -rf python/*.egg-info/

%build
%py_build

%install
%py_install

%files -n python-psautohint
%license COPYING LICENSE
%doc README.md
%{_bindir}/psautohint
%{_bindir}/psstemhist
%{python3_sitearch}/psautohint/
