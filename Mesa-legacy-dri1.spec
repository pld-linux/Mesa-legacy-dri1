# TODO: is separate libGL needed for DRI1 versions, or libGL 8.x is still compatible?
#
# Conditonal build:
%bcond_with	static_libs	# build static libGL
#
# minimal supported xserver version
%define		xserver_ver	1.5.0
# glapi version (glapi tables in dri drivers and libglx must be in sync);
# set to current Mesa version on ABI break, when xserver tables get regenerated
# (until they start to be somehow versioned themselves)
%define		glapi_ver	7.1.0
#
%define		libdrm_ver	2.4.25
%define		dri2proto_ver	2.6
%define		glproto_ver	1.4.11
#
Summary:	Free OpenGL implementation - legacy version for DRI1 drivers
Summary(pl.UTF-8):	Wolnodostępna implementacja standardu OpenGL - starsza wersja ze sterownikami DRI1
Name:		Mesa-legacy-dri1
Version:	7.11.2
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{version}/MesaLib-%{version}.tar.bz2
# Source0-md5:	0837c52698fe3252369c3fdb5195afcc
Patch0:		Mesa-realclean.patch
Patch1:		Mesa-selinux.patch
URL:		http://www.mesa3d.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	gcc >= 5:3.3
BuildRequires:	libdrm-devel >= %{libdrm_ver}
BuildRequires:	libselinux-devel
BuildRequires:	libstdc++-devel >= 5:3.3.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-libxml2
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.470
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.5
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-proto-dri2proto-devel >= %{dri2proto_ver}
BuildRequires:	xorg-proto-glproto-devel >= %{glproto_ver}
BuildRequires:	xorg-util-makedepend
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

This package contains legacy version for DRI1 drivers.

%description -l pl.UTF-8
Mesa jest biblioteką grafiki 3D z API bardzo podobnym do OpenGL(R). Do
tego stopnia, że Mesa używa składni i automatu OpenGL jest używana z
autoryzacją Silicon Graphics, Inc. Jednak autor nie posiada licencji
OpenGL od SGI i nie twierdzi, że Mesa jest kompatybilnym zamiennikiem
OpenGL ani powiązana z SGI.

Ten pakiet zawiera starszą wersję ze sterownikami DRI1.

%package libGL
Summary:	Free Mesa3D implementation of libGL OpenGL library
Summary(pl.UTF-8):	Wolnodostępna implementacja Mesa3D biblioteki libGL ze standardu OpenGL
Group:		X11/Libraries
Requires:	libdrm >= %{libdrm_ver}
Provides:	OpenGL = 2.1
Provides:	OpenGL-GLX = 1.4
Obsoletes:	Mesa
Obsoletes:	Mesa-dri
Obsoletes:	X11-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-OpenGL-libGL < 1:7.0.0

%description libGL
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

This package contains libGL which implements OpenGL 1.5 and GLX 1.4
specifications. It uses DRI for rendering.

%description libGL -l pl.UTF-8
Mesa jest biblioteką grafiki 3D z API bardzo podobnym do OpenGL(R). Do
tego stopnia, że Mesa używa składni i automatu OpenGL jest używana z
autoryzacją Silicon Graphics, Inc. Jednak autor nie posiada licencji
OpenGL od SGI i nie twierdzi, że Mesa jest kompatybilnym zamiennikiem
OpenGL ani powiązana z SGI.

Ten pakiet zawiera libGL implementującą specyfikacje OpenGL 1.5 oraz
GLX 1.4. Używa DRI do renderowania.

%package libGL-devel
Summary:	Header files for Mesa3D libGL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libGL z projektu Mesa3D
Group:		X11/Development/Libraries
# loose dependency on libGL to use with other libGL binaries
Requires:	OpenGL >= 1.5
Requires:	libdrm-devel >= %{libdrm_ver}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXxf86vm-devel
Requires:	xorg-proto-dri2proto-devel >= %{dri2proto_ver}
Requires:	xorg-proto-glproto-devel >= %{glproto_ver}
Suggests:	OpenGL-doc-man
Provides:	OpenGL-GLX-devel = 1.4
Provides:	OpenGL-devel = 2.1
Obsoletes:	Mesa-devel
Obsoletes:	X11-OpenGL-devel < 1:7.0.0
Obsoletes:	X11-OpenGL-devel-base < 1:7.0.0
Obsoletes:	XFree86-OpenGL-devel < 1:7.0.0
Obsoletes:	XFree86-OpenGL-devel-base < 1:7.0.0

%description libGL-devel
Header files for Mesa3D libGL library.

%description libGL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libGL z projektu Mesa3D.

%package libGL-static
Summary:	Static Mesa3D libGL library
Summary(pl.UTF-8):	Statyczna biblioteka libGL z projektu Mesa3D
Group:		X11/Development/Libraries
Requires:	%{name}-libGL-devel = %{version}-%{release}
Provides:	OpenGL-static = 2.1
Obsoletes:	Mesa-static
Obsoletes:	X11-OpenGL-static < 1:7.0.0
Obsoletes:	XFree86-OpenGL-static < 1:7.0.0

%description libGL-static
Static Mesa3D libGL library. It uses software renderer.

%description libGL-static -l pl.UTF-8
Statyczna biblioteka libGL z projektu Mesa3D. Używa programowego
renderingu.

%package -n Mesa-dri-driver-ati-mach64
Summary:	X.org DRI1 driver for ATI Mach64 card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart ATI Mach64
Group:		X11/Libraries
Requires:	xorg-driver-video-mach64
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}

%description -n Mesa-dri-driver-ati-mach64
X.org DRI1 driver for ATI Mach64 card family.

%description -n Mesa-dri-driver-ati-mach64 -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart ATI Mach64.

%package -n Mesa-dri-driver-ati-rage128
Summary:	X.org DRI1 driver for ATI Rage128 card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart ATI Rage128
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-r128
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-r128-dri < 1:7.0.0

%description -n Mesa-dri-driver-ati-rage128
X.org DRI1 driver for ATI Rage128 card family.

%description -n Mesa-dri-driver-ati-rage128 -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart ATI Rage128.

%package -n Mesa-dri-driver-ffb
Summary:	X.org DRI1 driver for Sun FFB card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart Sun FFB
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-sunffb
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}

%description -n Mesa-dri-driver-ffb
X.org DRI1 driver for SUN Creator3D and Elite3D card family.

%description -n Mesa-dri-driver-ffb -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart SUN Creator3D i Elite3D.

%package -n Mesa-dri-driver-glint
Summary:	X.org DRI1 driver for GLINT/Permedia card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart GLINT/Permedia
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-glint
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-glint-dri < 1:7.0.0

%description -n Mesa-dri-driver-glint
X.org DRI1 driver for GLINT/Permedia card family.

%description -n Mesa-dri-driver-glint -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart GLINT/Permedia.

%package -n Mesa-dri-driver-intel-i810
Summary:	X.org DRI1 driver for Intel i810 card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart Intel i810
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-i810-dri < 1:7.0.0

%description -n Mesa-dri-driver-intel-i810
X.org DRI1 driver for Intel i810 card family.

%description -n Mesa-dri-driver-intel-i810 -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart Intel i810.

%package -n Mesa-dri-driver-matrox
Summary:	X.org DRI1 driver for Matrox G card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart Matrox G
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-mga
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-mga-dri < 1:7.0.0

%description -n Mesa-dri-driver-matrox
X.org DRI1 drivers for Matrox G card family.

%description -n Mesa-dri-driver-matrox -l pl.UTF-8
Sterowniki X.org DRI1 dla rodziny kart Matrox G.

%package -n Mesa-dri-driver-savage
Summary:	X.org DRI1 driver for S3 Savage card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart S3 Savage
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-savage
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}

%description -n Mesa-dri-driver-savage
X.org DRI1 driver for S3 Savage card family.

%description -n Mesa-dri-driver-savage -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart S3 Savage.

%package -n Mesa-dri-driver-sis
Summary:	X.org DRI1 driver for SiS card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart SiS
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-sis
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-sis-dri < 1:7.0.0

%description -n Mesa-dri-driver-sis
X.org DRI1 driver for SiS card family.

%description -n Mesa-dri-driver-sis -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart SiS.

%package -n Mesa-dri-driver-tdfx
Summary:	X.org DRI1 driver for 3DFX Voodoo card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart 3DFX Voodoo
License:	MIT
Group:		X11/Libraries
Requires:	Glide3-DRI
Requires:	xorg-driver-video-tdfx
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Obsoletes:	X11-driver-tdfx-dri < 1:7.0.0

%description -n Mesa-dri-driver-tdfx
X.org DRI1 driver for 3DFX Voodoo card family (Voodoo 3,4,5, Banshee
and Velocity 100/200).

%description -n Mesa-dri-driver-tdfx -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart 3DFX Voodoo. (Voodoo 3,4,5,
Banshee i Velocity 100/200).

%package -n Mesa-dri-driver-via-unichrome
Summary:	X.org DRI1 driver for VIA Unichrome card family
Summary(pl.UTF-8):	Sterownik X.org DRI1 dla rodziny kart VIA Unichrome
License:	MIT
Group:		X11/Libraries
Requires:	xorg-driver-video-openchrome
Requires:	xorg-xserver-libglx(glapi) = %{glapi_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}

%description -n Mesa-dri-driver-via-unichrome
X.org DRI1 driver for VIA Unichrome card family.

%description -n Mesa-dri-driver-via-unichrome -l pl.UTF-8
Sterownik X.org DRI1 dla rodziny kart VIA Unichrome.

%prep
%setup -q -n Mesa-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}

dri_drivers="i810 mach64 mga r128 savage \
%ifarch sparc sparcv9 sparc64
ffb \
%endif
%ifarch %{ix86} %{x8664}
sis \
%endif
tdfx unichrome"

dri_drivers=$(echo $dri_drivers | xargs | tr ' ' ',')

%configure \
	--disable-egl \
	--disable-glu \
	--disable-glut \
	--disable-glw \
	--enable-glx-tls \
	--enable-pic \
	--enable-selinux \
	%{?with_static_libs:--enable-static} \
	--with-driver=dri \
	--with-dri-drivers=${dri_drivers} \
	--with-dri-driverdir=%{_libdir}/xorg/modules/dri \
	--without-gallium-drivers

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# libs without drivers
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# strip out undesirable headers
%{__rm} $RPM_BUILD_ROOT%{_includedir}/GL/{glfbdev,mesa_wgl,vms_x_fix,wglext,wmesa}.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	libGL -p /sbin/ldconfig
%postun	libGL -p /sbin/ldconfig

# see TODO question
%if 0
%files libGL
%defattr(644,root,root,755)
%doc docs/{*.html,README.{3DFX,GGI,MITS,QUAKE,THREADS},RELNOTES*}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
# symlink for binary apps which fail to conform Linux OpenGL ABI
# (and dlopen libGL.so instead of libGL.so.1; the same does Mesa libEGL)
%attr(755,root,root) %{_libdir}/libGL.so

%files libGL-devel
%defattr(644,root,root,755)
%doc docs/*.spec
%dir %{_includedir}/GL
%{_includedir}/GL/gl.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/glx_mangle.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_pkgconfigdir}/dri.pc
%{_pkgconfigdir}/gl.pc

%if %{with static_libs}
%files libGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%endif
%endif

%files -n Mesa-dri-driver-ati-mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/mach64_dri.so

%files -n Mesa-dri-driver-ati-rage128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/r128_dri.so

# sunffb (sparc only)
%ifarch sparc sparcv9 sparc64
%files -n Mesa-dri-driver-ffb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/ffb_dri.so
%endif

# glint (requires update)
%if 0
%files -n Mesa-dri-driver-glint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/gamma_dri.so
%endif

%files -n Mesa-dri-driver-intel-i810
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i810_dri.so

%files -n Mesa-dri-driver-matrox
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/mga_dri.so

%files -n Mesa-dri-driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/savage_dri.so

%ifarch %{ix86} %{x8664}
%files -n Mesa-dri-driver-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/sis_dri.so
%endif

%files -n Mesa-dri-driver-tdfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/tdfx_dri.so

%files -n Mesa-dri-driver-via-unichrome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/unichrome_dri.so
