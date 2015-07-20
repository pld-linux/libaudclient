%define		pre	rc2
%define		rel	1
Summary:	Audacious D-Bus remote control library
Name:		libaudclient
Version:	3.5
Release:	0.%{rc}.%{rel}
License:	BSD
Group:		Libraries
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}-%{pre}.tar.bz2
# Source0-md5:	5c7006c39091226180c320e253270653
URL:		http://audacious-media-player.org/
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious D-Bus remote control library.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{name}-%{version}-%{pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/audacious/*.h
%{_pkgconfigdir}/audclient.pc
