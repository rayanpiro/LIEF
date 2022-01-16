/* Copyright 2017 - 2021 R. Thomas
 * Copyright 2017 - 2021 Quarkslab
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#include "pyErr.hpp"

void init_LIEF_errors(py::module& m) {
  py::enum_<lief_errors>(m, "lief_errors", R"delim(
  Enum class which represents an error generated by LIEF's functions
  )delim")
    .value("read_error",        lief_errors::read_error)
    .value("not_found",         lief_errors::not_found)
    .value("not_implemented",   lief_errors::not_implemented)
    .value("not_supported",     lief_errors::not_supported)
    .value("corrupted",         lief_errors::corrupted)
    .value("conversion_error",  lief_errors::conversion_error)
    .value("read_out_of_bound", lief_errors::read_out_of_bound)
    .value("asn1_bad_tag",      lief_errors::asn1_bad_tag)
    .value("file_error",        lief_errors::file_error)
    .value("file_format_error", lief_errors::file_format_error)
  ;
}
