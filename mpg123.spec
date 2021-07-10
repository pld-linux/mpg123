#
# Conditional build:
%bcond_with	esd		# enable EsounD support
%bcond_without	alsa		# disable alsa support
%bcond_with	arts		# enable aRts support
%bcond_without	jack		# disable jack support
%bcond_without	nas		# diasble nas support
%bcond_without	openal		# disable openal support
%bcond_without	sdl		# disable sdl support
%bcond_without	portaudio	# disable portaudio support
%bcond_without	pulseaudio	# disable pulseaudio support
%bcond_with	tinyalsa	# enable tinyalsa support
%bcond_without	static_libs	# static library

Summary:	MPEG audio player
Summary(es.UTF-8):	Ejecuta archivos MP3
Summary(pl.UTF-8):	Odtwarzacz plików audio MPEG
Summary(pt_BR.UTF-8):	Tocador de arquivos MP3
Summary(ru.UTF-8):	Проигрыватель MPEG аудиофайлов
Summary(uk.UTF-8):	Програвач MPEG аудіофайлів
Name:		mpg123
Version:	1.28.1
Release:	1
# some old parts are GPLed, but they are not included in package
License:	LGPL v2.1
Group:		Applications/Sound
Source0:	https://downloads.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
# Source0-md5:	521f1e00d0814e8bc4b2a7129c340c8f
URL:		http://www.mpg123.de/
%{?with_openal:BuildRequires:	OpenAL-devel}
%{?with_sdl:BuildRequires:	SDL2-devel >= 2.0}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.7
%{?with_esd:BuildRequires:	esound-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 2:1.5
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel >= 18}
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
%{?with_tinyalsa:BuildRequires:	tinyalsa-devel}
%ifarch %{x8664}
BuildRequires:	yasm
%endif
Requires:	libmpg123 = %{version}-%{release}
Suggests:	%{name}-alsa = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%description -l es.UTF-8
Ejecuta archivos MP3.

%description -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach i486.

%description -l pt_BR.UTF-8
O mpg123 é um tocador de áudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos "MP3").

%description -l ru.UTF-8
Mpg123 - это быстрый, свободный и переносимый проигрыватель MPEG
аудиофайлов. он поддерживает MPEG 1.0/2.0 уровней 1, 2 и 3 ("MP3"
файлы). Для получения качества звучания компакт-диска (44 kHz, 16 бит,
стерео) ноеобходим процессор Pentium. Монозвук или звук худшего
качества (22 kHz или 11 kHz) возможен и на процессорах класса i486.

%description -l uk.UTF-8
Mpg123 - це швидкий, вільний та переносимий програвач MPEG
аудіофайлів. Він підтримує MPEG 1.0/2.0 рівнів 1, 2 та 3 ("MP3"
файли). Для отримання якості звучання компакт-диску (44 kHz, 16 біт,
стерео) необхідний процесор Pentium. Монозвук чи звук гіршої якості
(22 kHz чи 11 kHz) можливий і на процесорах класу i486.

%package alsa
Summary:	ALSA audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku ALSA dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description alsa
ALSA audio output plugin for mpg123.

%description alsa -l pl.UTF-8
Wtyczka wyjścia dźwięku ALSA dla mpg123.

%package arts
Summary:	aRts audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku aRts dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description arts
aRts audio output plugin for mpg123.

%description arts -l pl.UTF-8
Wtyczka wyjścia dźwięku aRts dla mpg123.

%package esd
Summary:	EsounD audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku EsounD dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description esd
EsounD audio output plugin for mpg123.

%description esd -l pl.UTF-8
Wtyczka wyjścia dźwięku EsounD dla mpg123.

%package jack
Summary:	JACK audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku JACK dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description jack
JACK audio output plugin for mpg123.

%description jack -l pl.UTF-8
Wtyczka wyjścia dźwięku JACK dla mpg123.

%package nas
Summary:	NAS audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku NAS dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description nas
NAS audio output plugin for mpg123.

%description nas -l pl.UTF-8
Wtyczka wyjścia dźwięku NAS dla mpg123.

%package openal
Summary:	OpenAL audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku OpenAL dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description openal
OpenAL audio output plugin for mpg123.

%description openal -l pl.UTF-8
Wtyczka wyjścia dźwięku OpenAL dla mpg123.

%package portaudio
Summary:	PortAudio audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku PortAudio dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description portaudio
PortAudio audio output plugin for mpg123.

%description portaudio -l pl.UTF-8
Wtyczka wyjścia dźwięku PortAudio dla mpg123.

%package pulseaudio
Summary:	PulseAudio audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku PulseAudio dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description pulseaudio
PulseAudio audio output plugin for mpg123.

%description pulseaudio -l pl.UTF-8
Wtyczka wyjścia dźwięku PulseAudio dla mpg123.

%package sdl
Summary:	SDL audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku SDL dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description sdl
SDL audio output plugin for mpg123.

%description sdl -l pl.UTF-8
Wtyczka wyjścia dźwięku SDL dla mpg123.

%package tinyalsa
Summary:	tinyalsa audio output plugin for mpg123
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku tinyalsa dla mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tinyalsa
tinyalsa audio output plugin for mpg123.

%description tinyalsa -l pl.UTF-8
Wtyczka wyjścia dźwięku tinyalsa dla mpg123.

%package -n libmpg123
Summary:	An optimized MPEG Audio decoder library
Summary(pl.UTF-8):	Zoptymalizowana biblioteka dekodera dźwięku MPEG
Group:		Libraries

%description -n libmpg123
An optimized MPEG Audio decoder library.

%description -n libmpg123 -l pl.UTF-8
Zoptymalizowana biblioteka dekodera dźwięku MPEG.

%package -n libmpg123-devel
Summary:	Header file for mpg123 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki mpg123
Group:		Development/Libraries
Requires:	libmpg123 = %{version}-%{release}

%description -n libmpg123-devel
Header file for mpg123 library.

%description -n libmpg123-devel -l pl.UTF-8
Plik nagłówkowy biblioteki mpg123.

%package -n libmpg123-static
Summary:	Static mpg123 library
Summary(pl.UTF-8):	Statyczna biblioteka mpg123
Group:		Development/Libraries
Requires:	libmpg123-static = %{version}-%{release}

%description -n libmpg123-static
Static mpg123 library.

%description -n libmpg123-static -l pl.UTF-8
Statyczna biblioteka mpg123.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# select "0" optimization, which doesn't add any -O to CFLAGS
%configure \
	--enable-modules \
	%{?with_static_libs:--enable-static} \
	--with-audio=%{?with_alsa:alsa,}oss%{?with_esd:,esd}%{?with_jack:,jack}%{?with_portaudio:,portaudio}%{?with_pulseaudio:,pulse}%{?with_sdl:,sdl}%{?with_nas:,nas}%{?with_arts:,arts}%{?with_openal:,openal}%{?with_tinyalsa:,tinyalsa} \
	--with-default-audio=%{?with_alsa:alsa,}oss \
	--with-optimization=0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libmpg123 -p /sbin/ldconfig
%postun	-n libmpg123 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO doc/{ACCURACY,BENCHMARKING,BUGS,CONTACT,LICENSE,PATENTS,README.gain,README.remote,ROAD_TO_LGPL,THANKS}
%ifarch athlon
%doc doc/README.3DNOW
%endif
%attr(755,root,root) %{_bindir}/mpg123
%attr(755,root,root) %{_bindir}/mpg123-id3dump
%attr(755,root,root) %{_bindir}/mpg123-strip
%attr(755,root,root) %{_bindir}/out123

%dir %{_libdir}/mpg123
%attr(755,root,root) %{_libdir}/mpg123/output_dummy.so
%attr(755,root,root) %{_libdir}/mpg123/output_oss.so
%{_mandir}/man1/mpg123.1*
%{_mandir}/man1/out123.1*

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_alsa.so
%endif

%if %{with arts}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_arts.so
%endif

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_esd.so
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_jack.so
%endif

%if %{with nas}
%files nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_nas.so
%endif

%if %{with openal}
%files openal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_openal.so
%endif

%if %{with portaudio}
%files portaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_portaudio.so
%endif

%if %{with pulseaudio}
%files pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_pulse.so
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_sdl.so
%endif

%if %{with tinyalsa}
%files tinyalsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpg123/output_tinyalsa.so
%endif

%files -n libmpg123
%defattr(644,root,root,755)
%doc NEWS.libmpg123
%attr(755,root,root) %{_libdir}/libmpg123.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpg123.so.0
%attr(755,root,root) %{_libdir}/libout123.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libout123.so.0
%attr(755,root,root) %{_libdir}/libsyn123.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsyn123.so.0

%files -n libmpg123-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpg123.so
%attr(755,root,root) %{_libdir}/libout123.so
%attr(755,root,root) %{_libdir}/libsyn123.so
%{_includedir}/fmt123.h
%{_includedir}/mpg123.h
%{_includedir}/out123.h
%{_includedir}/syn123.h
%{_pkgconfigdir}/libmpg123.pc
%{_pkgconfigdir}/libout123.pc
%{_pkgconfigdir}/libsyn123.pc

%if %{with static_libs}
%files -n libmpg123-static
%defattr(644,root,root,755)
%{_libdir}/libmpg123.a
%{_libdir}/libout123.a
%{_libdir}/libsyn123.a
%endif
