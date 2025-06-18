Summary:	C++ header-only Prometheus client library
Summary(pl.UTF-8):	Biblioteka klienta Prometheusa z samych plików nagłówkowych C++
Name:		prometheus-cpp-lite
Version:	1.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/biaks/prometheus-cpp-lite/releases
Source0:	https://github.com/biaks/prometheus-cpp-lite/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	284064732a693846673b1852e75ae2cc
# git log -p --reverse v1.0..master
Patch0:		%{name}-git.patch
URL:		https://github.com/biaks/prometheus-cpp-lite
BuildRequires:	cmake >= 3.2
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a tool for quickly adding metrics (and profiling) functionality
to C++ projects.

Advantages:
- Written in pure C++,
- Header-only,
- Cross-platform,
- Compiles with C++ 11, C++ 14, C++ 17 standards,
- Several APIs for use in your projects,
- Saving metrics to a file (and then works with node_exporter) or
  sending via HTTP (uses header-only http-client-lite library),
- Possiblity to use different types for storing metrics data,
- Five types of metrics are supported: counter, gauge, summary,
  histogram and benchmark,
- Has detailed examples of use.

%description -l pl.UTF-8
Narzędzie do szybkiego dodawania funkcji metryk (i profilowania) do
projektów w C++.

Zalety:
- napisane w czystym C++
- składa się wyłącznie z plików nagłówkowych
- wieloplatformowe
- zgodne ze standardami C++ 11, C++ 14, C++ 17
- do użycia w projektach dostępne jest kilka API
- zapis metryk do pliku (działa z node_exporter) lub wysyłanie przez
  HTTP (wykorzystuje bibliotekę z samego pliku nagłówkowego
  http-client-lite)
- możliwość użycia różnych typów do przechowywania danych metryk
- obsługa pięciu typów metryk: licznik, miernik, podsumowanie,
  histogram, dane o wydajności
- szczegółowe przykłady użycia.

%package devel
Summary:	C++ header-only Prometheus client library
Summary(pl.UTF-8):	Biblioteka klienta Prometheusa z samych plików nagłówkowych C++
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7
Requires:	http-client-lite-devel
BuildArch:	noarch

%description devel
It is a tool for quickly adding metrics (and profiling) functionality
to C++ projects.

Advantages:
- Written in pure C++,
- Header-only,
- Cross-platform,
- Compiles with C ++ 11, C ++ 14, C ++ 17 standards,
- Has no third-party dependencies,
- Several APIs for use in your projects,
- Saving metrics to a file (and then works with node_exporter) or
  sending via HTTP (uses header-only http-client-lite library),
- Possiblity to use different types for storing metrics data,
- Five types of metrics are supported: counter, gauge, summary,
  histogram and benchmark,
- Has detailed examples of use.

%description devel -l pl.UTF-8
Narzędzie do szybkiego dodawania funkcji metryk (i profilowania) do
projektów w C++.

Zalety:
- napisane w czystym C++
- składa się wyłącznie z plików nagłówkowych
- wieloplatformowe
- zgodne ze standardami C++ 11, C++ 14, C++ 17
- do użycia w projektach dostępne jest kilka API
- zapis metryk do pliku (działa z node_exporter) lub wysyłanie przez
  HTTP (wykorzystuje bibliotekę z samego pliku nagłówkowego
  http-client-lite)
- możliwość użycia różnych typów do przechowywania danych metryk
- obsługa pięciu typów metryk: licznik, miernik, podsumowanie,
  histogram, dane o wydajności
- szczegółowe przykłady użycia.

%package simpleapi-devel
Summary:	Prometheus client Simple API library
Summary(pl.UTF-8):	Biblioteka Simple API klienta Prometheusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description simpleapi-devel
Prometheus client Simple API library.

%description simpleapi-devel -l pl.UTF-8
Biblioteka Simple API klienta Prometheusa.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/prometheus-cpp-lite}

# no cmake install, do it manually;
# use subdir to resolve conflict with prometheus-cpp-devel
cp -pr core/include/prometheus $RPM_BUILD_ROOT%{_includedir}/prometheus-cpp-lite

cp -p simpleapi/include/prometheus/simpleapi.h $RPM_BUILD_ROOT%{_includedir}/prometheus-cpp-lite/prometheus
cp -p build/simpleapi/libprometheus-cpp-simpleapi.a $RPM_BUILD_ROOT%{_libdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/prometheus-cpp-lite
%exclude %{_includedir}/prometheus-cpp-lite/prometheus/simpleapi.h
%{_examplesdir}/%{name}-%{version}

%files simpleapi-devel
%defattr(644,root,root,755)
%{_libdir}/libprometheus-cpp-simpleapi.a
%{_includedir}/prometheus-cpp-lite/prometheus/simpleapi.h
