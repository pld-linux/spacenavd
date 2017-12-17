# TODO:
# - PLD/SysV init script (see setup_init as base) + systemd job (see contrib/systemd/spacenavd.service)
# - run as non-root user?
Summary:	Free driver for 3Dconnexion 6dof devices
Summary(pl.UTF-8):	Wolnodostępny sterownik dla urządzeń 3DConnexion o 6 stopniach swobody
Name:		spacenavd
Version:	0.6
Release:	1
License:	GPL v3+
Group:		Daemons
Source0:	http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz
# Source0-md5:	7e2c04fb8dbb7d39b9ee7b64565e0c4f
URL:		http://spacenav.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spacenavd, is a free software replacement user-space driver (daemon),
for 3Dconnexion's space-something 6dof input devices. It's compatible
with the original 3dxsrv proprietary daemon provided by 3Dconnexion,
and works perfectly with any program that was written for the
3Dconnexion driver.

%description -l pl.UTF-8
Spacenavd to wolnodostępny sterownik (demon przestrzeni użytkownika)
dla przestrzennych urządzeń wejściowych 3Dconnexion o 6 stopniach
swobody. Jest zgodny z własnościowym demonem 3dxsrv dostarczanym przez
3Dconnexion i działa idealnie z każdym programem napisanym dla
sterownika 3Dconnexion.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	opt="%{rpmcflags}" \
	xlib="-lX11" \
	add_ldflags="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/spacenavd
%attr(755,root,root) %{_bindir}/spnavd_ctl
