Summary:	FUSE implementation for overlayfs
Name:		fuse-overlayfs
Version:	1.9
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: https://github.com/containers/fuse-overlayfs/releases
Source0:	https://github.com/containers/fuse-overlayfs/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c034606457c95a3d63e992fe594d90e0
URL:		https://github.com/containers/fuse-overlayfs
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	libfuse3-devel >= 3.2.1
%ifarch %{ix86} %{x8664} %{arm} aarch64 mips64 mips64le ppc64 ppc64le s390x
BuildRequires:	go-md2man
%endif
BuildRequires:	pkgconfig
Requires:	libfuse3-tools >= 3.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of overlay+shiftfs in FUSE for rootless containers.

%prep
%setup -q

%build
install -d build-aux
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md SECURITY.md
%attr(755,root,root) %{_bindir}/fuse-overlayfs
%{_mandir}/man1/fuse-overlayfs.1*
