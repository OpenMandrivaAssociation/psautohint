Name:		psautohint
Summary:	A standalone version of AFDKO’s autohinter
Version:	2.0.0
Release:	%mkrel 1
License:	ASL 2.0
Group:		Text tools
Url:		https://github.com/adobe-type-tools/psautohint
Source0:	https://github.com/adobe-type-tools/psautohint/releases/download/v%{version}/psautohint-%{version}.zip
Patch0:		psautohint-1.8.1-linking.patch
BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
psautohint is a standalone version of the autohinter from the Adobe Font
Development Kit for OpenType (AFDKO).

%package -n python3-psautohint
Summary:	Python library for standalone version of the AFDKO autohinter
Group:		Development/Python
Provides:	%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-psautohint}

%description -n python3-psautohint
psautohint is a standalone version of the autohinter from the Adobe Font
Development Kit for OpenType (AFDKO).

%prep
%autosetup -p1

# re-generate egg-info
rm -rf python/*.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-psautohint
%license COPYING LICENSE
%doc README.md
%{_bindir}/psautohint
%{_bindir}/psstemhist
%{python3_sitearch}/psautohint/
%{python3_sitearch}/psautohint-%{version}-py?.?.egg-info/
