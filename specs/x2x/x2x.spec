# $Id$

# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Link two X displays together, simulating a multiheaded display
Name: x2x
Version: 1.27
Release: 0
License: BSD
Group: User Interface/Desktops
URL: http://ftp.digital.com/pub/Digital/SRC/x2x/

Source: http://ftp.digital.com/pub/Digital/SRC/x2x/x2x-1.27.tar.gz
Patch: http://ftp.debian.org/debian/pool/main/x/x2x/x2x_1.27-8.diff.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
x2x joins a pair of X displays together, as if they were a single
multiheaded display. The pointer can be warped between displays, or,
depending on how you start x2x, can slide from one display to the
other when it runs off the edge of the screen. Keyboard focus also
moves between displays in the way you'd expect, and the X selection
propagates around. At least one of the displays involved
(specifically, the one being controlled remotely) must support the
XTEST extension.

%prep
%setup
%patch0 -p1
%{__mv} -f x2x.1 x2x.man

%build
xmkmf
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 x2x %{buildroot}%{_bindir}/x2x
%{__install} -Dp -m0755 x2x.man %{buildroot}%{_mandir}/man1/x2x.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/x2x.1*
%{_bindir}/x2x

%changelog
* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 1.27-0
- Initial package. (using DAR)
