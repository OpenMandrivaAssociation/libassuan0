%define major 0
%define libname %mklibname assuan %{major}
%define devname %mklibname assuan -d

Summary:	Old version of Assuan - an IPC library for non-persistent servers
Name:		libassuan0
Version:	2.5.7
Release:	1
License:	LGPLv3
Group:		System/Libraries
Url:		https://www.gnupg.org/
Source0:	https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	hostname
BuildSystem:	autotools

%description
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%package -n %{libname}
Summary:	An IPC library for non-persistent servers
Group:		System/Libraries
Obsoletes:	libassuan < 2.0.0-4
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%install -a
# No -devel stuff for compat packages
rm -rf \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_datadir} \
	%{buildroot}%{_libdir}/*.so \
	%{buildroot}%{_libdir}/pkgconfig \

%files -n %{libname}
%{_libdir}/libassuan.so.%{major}*
