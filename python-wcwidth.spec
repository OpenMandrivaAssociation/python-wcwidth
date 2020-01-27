%global pypi_name wcwidth

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        1
Summary:        Measures number of Terminal column cells of wide-character codes
Group:		Development/Java
License:        MIT
URL:            https://github.com/jquast/wcwidth
Source0:        https://pypi.io/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
 
%description
This API is mainly for Terminal Emulator implementors, or those writing 
programs that expect to interpreted by a terminal emulator and wish to 
determine the printable width of a string on a Terminal.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%buildroot

%files
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
