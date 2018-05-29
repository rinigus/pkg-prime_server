%global debug_package %{nil}

Summary: non-blocking (web)server API for distributed computing and SOA based on zeromq 
Name: prime_server
Version: 0.6.3
Release: 1%{?dist}
License: BSD
Group: Libraries/Network
URL: https://github.com/kevinkreiser/prime_server

#Source: https://github.com/kevinkreiser/prime_server/archive/0.6.3.tar.gz
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libtool
BuildRequires:zeromq-devel >= 4.1.4, czmq-devel >= 3.0, libcurl-devel >= 7.22.0
Requires: zeromq >= 4.1.4, czmq >= 3.0, libcurl >= 7.22.0

%description
non-blocking (web)server API for distributed computing and SOA based on zeromq 

%package devel
Summary: prime_server development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%package tools
Summary: prime_server tools
Group: Libraries/Network
Requires: %{name} = %{version}

%description tools
Tools for prime_server

%prep
%setup -q -n %{name}-%{version}/prime_server

%build
%{__make} clean || true
./autogen.sh

CFLAGS="$CFLAGS -fPIC -lpthread"
CXXFLAGS="$CXXFLAGS -fPIC -lpthread"
%configure

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n prime_server -p /sbin/ldconfig

%postun -n prime_server -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libprime_server.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/prime_server
%{_libdir}/libprime_server.a
%{_libdir}/libprime_server.la
%{_libdir}/pkgconfig/libprime_server.pc

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/prime_*

%changelog
* Sun Apr 29 2018 Martin Kolman <martin.kolman@gmail.com> - 0.6.3-1
- initial Fedora packaging
