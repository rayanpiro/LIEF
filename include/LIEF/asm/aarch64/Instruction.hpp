/* Copyright 2022 - 2024 R. Thomas
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
#ifndef LIEF_ASM_AARCH64_INST_H
#define LIEF_ASM_AARCH64_INST_H
#include "LIEF/visibility.h"

#include "LIEF/asm/Instruction.hpp"
#include "LIEF/asm/aarch64/opcodes.hpp"
#include "LIEF/asm/aarch64/Operand.hpp"

namespace LIEF {
namespace assembly {

/// AArch64 architecture-related namespace
namespace aarch64 {

/// This class represents an AArch64 instruction
class LIEF_API Instruction : public assembly::Instruction {
  public:
  using assembly::Instruction::Instruction;

  using operands_it = iterator_range<Operand::Iterator>;

  /// The instruction opcode as defined in LLVM
  OPCODE opcode() const;

  /// Iterator over the operands of the current instruction
  operands_it operands() const;

  /// True if `inst` is an **effective** instance of aarch64::Instruction
  static bool classof(const assembly::Instruction* inst);

  ~Instruction() override = default;
};
}
}
}
#endif
