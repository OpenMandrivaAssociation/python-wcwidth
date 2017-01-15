%global pypi_name wcwidth

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        1
Summary:        Measures number of Terminal column cells of wide-character codes
Group:		Development/Java
License:        MIT
URL:            https://github.com/jquast/wcwidth
Source0:        https://pypi.io/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%description
This API is mainly for Terminal Emulator implementors, or those writing 
programs that expect to interpreted by a terminal emulator and wish to 
determine the printable width of a string on a Terminal.

%package -n     python2-%{pypi_name}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Summary:        Measures number of Terminal column cells of wide-character codes

%prep
%setup -q -n %{pypi_name}-%{version}

cp -a . %py2dir

%build
python setup.py build
pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%buildroot
pushd %py2dir
python2 setup.py install --root=%buildroot

%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.6-2
- Provide python-wcwidth for EL6

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.6-1
- Update to new upstream
- Remove external LICENSE thanks to the new version

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-2
- Remove shabang from file that was not executable

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-1
- Initial package.
