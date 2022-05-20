%define _disable_source_fetch 0
%bcond_without check
#%global debug_package %{nil}

%global crate pop-launcher

Name:           %{crate}
Version:        1.2.1
Release:        %autorelease
Summary:        Library for writing plugins and frontends for pop-launcher

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/pop-launcher
Source:         https://github.com/pop-os/launcher/archive/refs/tags/%{version}.tar.gz
Source1:        vendor.tar
Source2:        cargo-config.tar.gz
Patch:          0001-Copy-instead-of-symlink.patch
Patch1:         0001-Remove-frozen-lock.patch

Provides:       rust-%{crate} = 1.2.1

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  just

%global _description %{expand:
Library for writing plugins and frontends for pop-launcher.}

%description %{_description}


%prep
%autosetup -n launcher-%{version_no_tilde}
%cargo_prep
#just vendor
cp %{SOURCE1} vendor.tar
#tar -xf vendor.tar
tar -xvf %{SOURCE2}
#%generate_buildrequires
#%cargo_generate_buildrequires

%build

just vendor=1

%install
just rootdir=%{buildroot} install

%if %{with check}
%check
%cargo_test
%endif


%files
%{_bindir}/pop-launcher
%{_prefix}/lib/pop-launcher/

%changelog
%autochangelog
