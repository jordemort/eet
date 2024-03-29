%{!?_rel:%{expand:%%global _rel 0.enl%{?dist}}}
%define _missing_doc_files_terminate_build 0

Summary: Library for speedy data storage, retrieval, and compression.
Name: eet
Version: 1.7.7
Release: %{_rel}
License: BSD
Group: System Environment/Libraries
Source: http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
Packager: %{?_packager:%{_packager}}%{!?_packager:Michael Jennings <mej@eterm.org>}
Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:The Enlightenment Project (http://www.enlightenment.org/)}
Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
URL: http://www.enlightenment.org/
BuildRequires: libjpeg-devel zlib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Eet is a tiny library designed to write an arbitrary set of chunks of
data to a file and optionally compress each chunk (very much like a
zip file) and allow fast random-access reading of the file later
on. It does not do zip as a zip itself has more complexity than is
needed, and it was much simpler to implement this once here.

It also can encode and decode data structures in memory, as well as
image data for saving to eet files or sending across the network to
other machines, or just writing to arbitrary files on the system. All
data is encoded in a platform independent way and can be written and
read by any architecture.

%package devel
Summary: Eet headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}
Requires: libjpeg-devel, zlib-devel

%description devel
Headers, static libraries, test programs and documentation for Eet

%prep
%setup -q

%build
%{configure} --prefix=%{_prefix}
### use this if you have build problems
#./configure --prefix=%{_prefix}
%{__make} %{?_smp_mflags} %{?mflags}

%install
%{__make} %{?mflags_install} DESTDIR=$RPM_BUILD_ROOT install

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING-PLAIN README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/eet*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/eet
%{_libdir}/*.la

%changelog
