use lief_ffi as ffi;

use crate::common::FromFFI;
use crate::assembly;
use super::Opcode;

/// This structure represents a x86/x86-64 instruction
pub struct Instruction {
    ptr: cxx::UniquePtr<ffi::asm_x86_Instruction>,
}

impl FromFFI<ffi::asm_x86_Instruction> for Instruction {
    fn from_ffi(ptr: cxx::UniquePtr<ffi::asm_x86_Instruction>) -> Self {
        Self {
            ptr,
        }
    }
}

impl assembly::Instruction for Instruction {
    #[doc(hidden)]
    fn as_generic(&self) -> &ffi::asm_Instruction {
        self.ptr.as_ref().unwrap().as_ref()
    }
}

impl Instruction {
    /// The instruction opcode as defined in LLVM
    pub fn opcode(&self) -> Opcode {
        Opcode::from(self.ptr.opcode())
    }
}
